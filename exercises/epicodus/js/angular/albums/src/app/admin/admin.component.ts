import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Album } from '../album.model';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css'],
  providers: [AlbumService]
})
<<<<<<< HEAD
=======

>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
export class AdminComponent implements OnInit {

  constructor(private albumService: AlbumService) { }

  ngOnInit() {
  }

<<<<<<< HEAD
  submitForm(title: string, artist: string, description: string) {
    var newAlbum: Album = new Album(title, artist, description);
=======
  submitForm(title: string, artist: string, description: string, price: string) {
    var newAlbum: Album = new Album(title, artist, description, parseInt(price));
>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
    this.albumService.addAlbum(newAlbum);
  }
}
