import { Component, OnInit, Input } from '@angular/core';
import { Player } from './player.class';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.css']
})
export class PlayerComponent implements OnInit {
  players: Player[];
  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.players.subscribe(players => {
      if (players) {
        this.players = players;
        console.log('First player: ', players[2]);
      } else {
        console.log('No plauers');
      }
    });
  }
}
