import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Socket } from 'ngx-socket-io';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-chat-room',
  templateUrl: './chat-room.page.html',
  styleUrls: ['./chat-room.page.scss'],
})
export class ChatRoomPage implements OnInit, OnDestroy {
  messages:any = [];
  nickname = '';
  message: string = '';

  constructor(private route: ActivatedRoute,
              private socket: Socket,
              private toastCtrl: ToastController) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      console.log(params)
      this.nickname = params['nickname'];
    });

    this.socket.on('message', (message: any) => this.messages.push(message));

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
