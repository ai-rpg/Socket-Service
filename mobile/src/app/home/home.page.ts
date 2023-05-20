import { Component } from '@angular/core';
import { Socket } from 'ngx-socket-io';
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
    this.router.navigateByUrl(`chat-room/${this.nickname}`);
  }

}
