import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  nickname = '';

  constructor(private router: Router)  { }

  joinChat() {
    // this.socket.connect();
    // this.socket.emit('set-nickname', this.nickname);
    this.router.navigateByUrl(`chat-room/${this.nickname}`);
  }

}
