import { Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Socket } from 'ngx-socket-io';
import { IonContent, ToastController } from '@ionic/angular';

@Component({
  selector: 'app-chat-room',
  templateUrl: './chat-room.page.html',
  styleUrls: ['./chat-room.page.scss'],
})
export class ChatRoomPage implements OnInit, OnDestroy {
  messages:any = [];
  nickname = '';
  message: string = '';
  @ViewChild(IonContent, {read: IonContent, static: false}) content: IonContent;

  constructor(private route: ActivatedRoute,
              private socket: Socket,
              private toastCtrl: ToastController) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      console.log(params)
      this.socket.connect();
      this.nickname = params['nickname'];
      this.socket.emit('set-nickname', this.nickname);
    });

    this.socket.on('message', (message: any) => {
      this.messages.push(message);
      this.ScrollToBottom();
    });

    this.socket.on('users-changed', (data: { [x: string]: string; }) => {
      console.log('here')
      const user = data['user'];
      if (data['event'] === 'left') {
        this.showToast('User left: ' + user);
      } else {
        this.showToast('User joined: ' + user);
      }
    });
  }

  ScrollToBottom(){
    setTimeout(() => {
      this.content.scrollToBottom(300);
   }, 1000);

  }

  sendMessage() {
    this.socket.emit('add-message', { text: this.message });
    this.message = '';
  }

  ngOnDestroy() {
    this.socket.disconnect();
  }

  async showToast(msg: string) {
    const toast = await this.toastCtrl.create({
      message: msg,
      duration: 2000
    });
    toast.present();
  }
}
