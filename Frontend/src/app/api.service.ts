import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { Player } from './components/player/player.class';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private playersSubject = new BehaviorSubject<Player[]>([]);
  constructor(private http: HttpClient) {}

  players = this.playersSubject.asObservable();

  doPlayersCheck() {
    const url = 'http://localhost:3000/';
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer 9f4daaa114b20d9c6a0d1713efc132c`,
      Accept: 'application/json'
    });

    /*     this.http
      .get<Player[]>(url, {
        headers: headers
      })
      .subscribe(response => {
        if (response) {
          this.playersSubject.next(response);
        } else {
        }
      }); */
  }
  doPlayersCheckTest() {
    this.playersSubject.next([
      new Player('Alex', 'Developer', 'asdsadasd '),
      new Player('Frans', 'Nerd', 'asddasg dihasi '),
      new Player('Niels', 'Robin to Nerd', 'gsdfasdihasi '),
      new Player('Prayson', 'Owner of something', 'Preyson is '),
      new Player(
        'Eskil',
        'Skilled in Electronics',
        'rerqrdafashd ohasiojd ahs dihasi '
      )
    ]);
  }
}
