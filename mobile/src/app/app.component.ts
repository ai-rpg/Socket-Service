import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  public appPages = [
    { title: 'Inbox', url: '/home', icon: 'mail' },
    { title: 'profile', url: '/profile', icon: 'paper-plane' },
    { title: 'public', url: '/public', icon: 'heart' },
    { title: 'protected', url: '/protected', icon: 'archive' },
    { title: 'admin', url: '/admin', icon: 'trash' },
    { title: 'callback', url: '/callback', icon: 'warning' },
  ];
  public labels = ['Family', 'Friends', 'Notes', 'Work', 'Travel', 'Reminders'];

  constructor() {}
}
