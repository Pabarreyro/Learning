import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { MarsRoverApiPhotosService } from '../mars-rover-api-photos.service';
import { PhotoService } from '../photo.service';

@Component({
  selector: 'app-rover-form',
  templateUrl: './rover-form.component.html',
  styleUrls: ['./rover-form.component.css'],
  providers: [MarsRoverApiPhotosService, PhotoService]
})

export class RoverFormComponent implements OnInit {
  photos: any[] = null;
  constructor(private marsRoverPhotos: MarsRoverApiPhotosService) { }

  getRoverImages(date: string, camera: string) {
    this.photos=null;
    this.marsRoverPhotos.getByDateAndCamera(date, camera).subscribe(response => {
      this.photos = response.json();
    })
  }

  saveRoverImages(date, camera){
    this.marsRoverPhotos.saveImages(date, camera);
    alert(`The images from ${date} taken by the ${camera} camera have been saved to the database.`)
  }

  ngOnInit() {
  }

}
