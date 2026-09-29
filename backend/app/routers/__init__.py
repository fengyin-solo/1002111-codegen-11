"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import pole as router_pole
from app.routers import lamp as router_lamp
from app.routers import cabinet as router_cabinet
from app.routers import brightening as router_brightening
from app.routers import repair as router_repair
from app.routers import meter as router_meter
from app.routers import cable as router_cable
from app.routers import anti_theft as router_anti_theft
from app.routers import acceptance as router_acceptance
from app.routers import schedule as router_schedule
from app.routers import controller as router_controller
from app.routers import emergency as router_emergency
from app.routers import patrol as router_patrol
from app.routers import plan as router_plan
from app.routers import landscape as router_landscape
from app.routers import complaint as router_complaint

ROUTERS = [router_pole, router_lamp, router_cabinet, router_brightening, router_repair, router_meter, router_cable, router_anti_theft, router_acceptance, router_schedule, router_controller, router_emergency, router_patrol, router_plan, router_landscape, router_complaint]
