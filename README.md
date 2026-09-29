# 城市照明设施运维管理平台

面向城市路灯杆、配电箱、亮化工程、报修排障、能耗监测、线路防盗与验收移交的一体化城市照明设施运维管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 路灯杆管理 | `pole` | 路灯杆 | 杆号、所在道路、灯型规格 |
| 灯具管理 | `lamp` | 灯具 | 灯具编号、所属灯杆、灯具品牌 |
| 配电箱管理 | `cabinet` | 配电箱 | 配电箱编号、安装位置、箱体类型 |
| 亮化工程 | `brightening` | 亮化项目 | 项目编号、项目名称、建筑载体 |
| 报修处理 | `repair` | 报修单 | 报修编号、报修位置、故障类型 |
| 能耗监测 | `meter` | 电表读数 | 电表编号、所属配电箱、抄表日期 |
| 电缆管理 | `cable` | 电缆 | 电缆编号、敷设方式、电缆型号 |
| 防盗监测 | `anti_theft` | 防盗设备 | 设备编号、安装位置、设备类型 |
| 验收移交 | `acceptance` | 验收单 | 验收编号、验收对象、移交单位 |
| 开关灯计划 | `schedule` | 开关灯方案 | 方案编号、适用路段、季节类型 |
| 智能终端 | `controller` | 终端设备 | 终端编号、终端型号、安装位置 |
| 应急保障 | `emergency` | 保障任务 | 任务编号、保障类型、保障区域 |
| 亮灯率巡检 | `patrol` | 巡检记录 | 记录编号、巡检路段、巡检日期 |
| 年度改造计划 | `plan` | 改造项目 | 项目编号、项目名称、改造路段 |
| 景观照明 | `landscape` | 景观照明设施 | 设施编号、设施名称、景观类型 |
| 市民投诉 | `complaint` | 投诉记录 | 投诉编号、投诉来源、投诉路段 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
