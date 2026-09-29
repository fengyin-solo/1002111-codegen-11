import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Pole = () => import('@/views/pole/index.vue')
const Lamp = () => import('@/views/lamp/index.vue')
const Cabinet = () => import('@/views/cabinet/index.vue')
const Brightening = () => import('@/views/brightening/index.vue')
const Repair = () => import('@/views/repair/index.vue')
const Meter = () => import('@/views/meter/index.vue')
const Cable = () => import('@/views/cable/index.vue')
const AntiTheft = () => import('@/views/anti_theft/index.vue')
const Acceptance = () => import('@/views/acceptance/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Controller = () => import('@/views/controller/index.vue')
const Emergency = () => import('@/views/emergency/index.vue')
const Patrol = () => import('@/views/patrol/index.vue')
const Plan = () => import('@/views/plan/index.vue')
const Landscape = () => import('@/views/landscape/index.vue')
const Complaint = () => import('@/views/complaint/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/pole', name: 'pole', component: Pole },
    { path: '/lamp', name: 'lamp', component: Lamp },
    { path: '/cabinet', name: 'cabinet', component: Cabinet },
    { path: '/brightening', name: 'brightening', component: Brightening },
    { path: '/repair', name: 'repair', component: Repair },
    { path: '/meter', name: 'meter', component: Meter },
    { path: '/cable', name: 'cable', component: Cable },
    { path: '/anti_theft', name: 'anti_theft', component: AntiTheft },
    { path: '/acceptance', name: 'acceptance', component: Acceptance },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/controller', name: 'controller', component: Controller },
    { path: '/emergency', name: 'emergency', component: Emergency },
    { path: '/patrol', name: 'patrol', component: Patrol },
    { path: '/plan', name: 'plan', component: Plan },
    { path: '/landscape', name: 'landscape', component: Landscape },
    { path: '/complaint', name: 'complaint', component: Complaint },
  ],
})

export default router
