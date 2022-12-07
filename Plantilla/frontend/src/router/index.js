import Vue from 'vue';
import Router from 'vue-router';

import Dashboard from '../pages/Dashboard.vue';
import Social from '../pages/Social.vue';
import Media from '../pages/Media.vue';
import Snackbar from '../pages/Snackbar.vue';
import Chart from '../pages/Chart.vue';
import Cursos from '../pages/Cursos.vue';
import Schedulle from '../pages/Schedulle.vue';
import Login from '../pages/core/Login.vue';
import Error from '../pages/core/Error.vue';
import Usuarios from '../pages/Usuarios.vue';
import Estudiantes from '../pages/Estudiantes.vue';
import Profesores from '../pages/Profesores.vue';
import Participation from '../pages/Participation.vue';
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      meta: {
        breadcrumb: [
          { name: 'dashboard' }
        ]
      }
    },
    {
      path: '/cursos',
      name: 'Cursos',
      component: Cursos,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'Cursos' }
        ]
      }
    },
    {
      path: '/estudiantes',
      name: 'Estudiantes',
      component: Estudiantes,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'Estudiantes' }
        ]
      }
    },
    {
      path: '/profesores',
      name: 'Profesores',
      component: Profesores,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'Profesores' }
        ]
      }
    },
    {
      path: '/usuarios',
      name: 'Usuarios',
      component: Usuarios,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'Usuarios' }
        ]
      }
    },
    {
      path: '/participation',
      name: 'Participation',
      component: Participation,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'Participation' }
        ]
      }
    },
    {
      path: '/snackbar',
      name: 'Snackbar',
      component: Snackbar,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'snackbar' }
        ]
      }
    },
    {
      path: '/schedulle',
      name: 'Schedulle',
      component: Schedulle,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'Schedulle' }
        ]
      }
    },
    {
      path: '/social',
      name: 'Social',
      component: Social,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'social' }
        ]
      }
    },
    {
      path: '/media',
      name: 'Media',
      component: Media,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'media' }
        ]
      }
    },
    {
      path: '/chart',
      name: 'Chart',
      component: Chart,
      meta: {
        breadcrumb: [
          { name: 'dashboard', href: 'Dashboard' },
          { name: 'charts' }
        ]
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        allowAnonymous: true
      }
    },
    {
      path: '/error',
      name: 'Error',
      component: Error,
      meta: {
        allowAnonymous: true
      }
    },
  ]
});
