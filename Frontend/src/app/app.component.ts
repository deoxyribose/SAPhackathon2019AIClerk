import { Component, OnInit, OnDestroy } from '@angular/core';
import { Player } from './components/player/player.class';
import { ApiService } from './api.service';
import { interval, Subscription } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  subscription: Subscription;
  constructor(private apiService: ApiService) {
    const source = interval(1000);
    this.subscription = source.subscribe(val =>
      this.apiService.doPlayersCheck()
    );
  }
  ngOnInit() {
    this.apiService.doPlayersCheckTest();
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
