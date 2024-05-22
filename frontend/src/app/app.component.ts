import { CommonModule } from '@angular/common';
import { AfterViewInit, Component, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { HeaderComponent } from './pages/user/header/header.component';
import { initFlowbite } from 'flowbite';
import { isPlatformBrowser } from '@angular/common';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, HeaderComponent, RouterLink],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements AfterViewInit{
  title = 'frontend';

  constructor(@Inject(PLATFORM_ID) private platformId: Object) { }
  ngAfterViewInit() {
    if (isPlatformBrowser(this.platformId)) {
      // Este código solo se ejecutará en el navegador
      initFlowbite();
    }
  }
}
