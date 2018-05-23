import { Component, OnInit } from '@angular/core';
<<<<<<< HEAD
import { Album } from '../album.model';
import { Router } from '@angular/router';
import { AlbumService } from '../album.service';
=======
import { Router } from '@angular/router';
import { AlbumService } from '../album.service';
import { Album } from '../album.model';
>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
import { FirebaseListObservable } from 'angularfire2/database';

@Component({
  selector: 'app-marketplace',
  templateUrl: './marketplace.component.html',
  styleUrls: ['./marketplace.component.css'],
  providers: [AlbumService]
})

export class MarketplaceComponent implements OnInit {
  albums: FirebaseListObservable<any[]>;
<<<<<<< HEAD

  constructor(private router: Router, private albumService: AlbumService){}

  ngOnInit(){
    this.albums = this.albumService.getAlbums();
  }

  goToDetailPage(clickedAlbum) {
    this.router.navigate(['albums', clickedAlbum.$key]);
  };
=======
  currentRoute: string = this.router.url;
  filterByPrice: string = "all";
  showEdit: boolean = false;
  shownAlbum = null;

  constructor(private router: Router, private albumService: AlbumService) {}

  goToDetailPage(clickedAlbum) {
    this.router.navigate(['albums', clickedAlbum.$key]);
  }

  onChange(filterPrice) {
    if (filterPrice === 'pricey') {
      this.albums = this.albumService.getFilteredAlbums(50, 1000);
    } else if (filterPrice === 'midrange') {
      this.albums = this.albumService.getFilteredAlbums(20, 50);
    } else if (filterPrice === 'cheap') {
      this.albums = this.albumService.getFilteredAlbums(0, 20);
    } else {
      this.albums = this.albumService.getAlbums(); 
    }
  }

  displayEdit(album){
    this.clearDisplay();
    this.showEdit = true;
    this.shownAlbum = album;
  }

  clearDisplay() {
    this.shownAlbum = null;
    this.showEdit = false;
  }

  ngOnInit() {
    this.albums = this.albumService.getAlbums();
  }
>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
}
