import { Component, OnInit} from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { ImageModule } from 'primeng/image';
@Component({
  selector: 'app-init-page',
  standalone: true,
  imports: [ButtonModule, ImageModule],
  templateUrl: './init-page.component.html',
  styleUrl: './init-page.component.css'
})
export class InitPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {

  }
}
