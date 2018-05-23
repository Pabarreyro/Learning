import { Injectable } from '@angular/core';
import { Album } from './album.model';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

@Injectable()
export class AlbumService {
  albums: FirebaseListObservable<any[]>;

  constructor(private database: AngularFireDatabase) {
    this.albums = database.list('albums');
  }

<<<<<<< HEAD
=======
  getAlbumById(albumId: string){
    return this.database.object('albums/' + albumId);
  }

>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
  getAlbums() {
    return this.albums;
  }

<<<<<<< HEAD
  addAlbum(newAlbum: Album){
    this.albums.push(newAlbum);
  }

  getAlbumById(albumId: string) {
    return this.database.object('albums/' + albumId)
  }
=======
  getFilteredAlbums(startNum: number, endNum: number) {
    return this.albums = this.database.list('albums', {
      query: {
        orderByChild: 'price',
        startAt: startNum,
        endAt: endNum
      }
    });
  }

  addAlbum(newAlbum: Album) {
    this.albums.push(newAlbum);
  }

  updateAlbum(localUpdatedAlbum){
    let albumEntryInFireBase = this.getAlbumById(localUpdatedAlbum.$key);
    albumEntryInFireBase.update({title: localUpdatedAlbum.title,
                                artist: localUpdatedAlbum.artist,
                                description: localUpdatedAlbum.description});
  }

  deleteAlbum(localUpdatedAlbum){
    let albumEntryInFireBase = this.getAlbumById(localUpdatedAlbum.$key);
    albumEntryInFireBase.remove();
  }

>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
}
