<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">城市照明设施运维管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向城市路灯杆、配电箱、亮化工程、报修排障、能耗监测、线路防盗与验收移交的一体化城市照明设施运维管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "路灯杆管理", path: "/pole" }, { label: "灯具管理", path: "/lamp" }, { label: "配电箱管理", path: "/cabinet" }, { label: "亮化工程", path: "/brightening" }, { label: "报修处理", path: "/repair" }, { label: "能耗监测", path: "/meter" }, { label: "电缆管理", path: "/cable" }, { label: "防盗监测", path: "/anti_theft" }, { label: "验收移交", path: "/acceptance" }, { label: "开关灯计划", path: "/schedule" }, { label: "智能终端", path: "/controller" }, { label: "应急保障", path: "/emergency" }, { label: "亮灯率巡检", path: "/patrol" }, { label: "年度改造计划", path: "/plan" }, { label: "景观照明", path: "/landscape" }, { label: "市民投诉", path: "/complaint" }]
</script>
