import { isPlatformBrowser } from '@angular/common';
import { Component, Inject, OnInit, PLATFORM_ID} from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { ImageModule } from 'primeng/image';
import { HeaderComponent } from '../../user/header/header.component';
import { RouterOutlet } from '@angular/router';
import { UserFooterComponent } from '../../user/user-footer/user-footer.component';
@Component({
  selector: 'app-init-page',
  standalone: true,
  imports: [ButtonModule, ImageModule, HeaderComponent, RouterOutlet, UserFooterComponent],
  templateUrl: './init-page.component.html',
  styleUrl: './init-page.component.css'
})
export class InitPageComponent implements OnInit {

  constructor(@Inject(PLATFORM_ID) private platformId: object) { }

  ngOnInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      setTimeout(() => {
        const content = document.getElementById('content');
        if (content) {
          content.classList.add('visible');
        }
      }, 100);
    }
  }
}
