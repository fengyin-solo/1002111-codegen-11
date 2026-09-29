"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PoleEntry(BaseModel):
    """路灯杆明细结构。"""

    field_0: str | None = None  # 杆号
    field_1: str | None = None  # 所在道路
    field_2: str | None = None  # 灯型规格
    field_3: str | None = None  # 灯杆高度
    field_4: str | None = None  # 光源类型
    field_5: str | None = None  # 安装日期
    field_6: str | None = None  # 产权单位
    field_7: str | None = None  # 杆体状态

class LampEntry(BaseModel):
    """灯具明细结构。"""

    field_0: str | None = None  # 灯具编号
    field_1: str | None = None  # 所属灯杆
    field_2: str | None = None  # 灯具品牌
    field_3: str | None = None  # 额定功率
    field_4: str | None = None  # 光通量
    field_5: str | None = None  # 色温
    field_6: str | None = None  # 更换日期
    field_7: str | None = None  # 运行状态

class CabinetEntry(BaseModel):
    """配电箱明细结构。"""

    field_0: str | None = None  # 配电箱编号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 箱体类型
    field_3: str | None = None  # 回路数量
    field_4: str | None = None  # 额定电流
    field_5: str | None = None  # 安装日期
    field_6: str | None = None  # 防雷等级
    field_7: str | None = None  # 运行状态

class BrighteningEntry(BaseModel):
    """亮化项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 建筑载体
    field_3: str | None = None  # 灯具类型
    field_4: str | None = None  # 承建方
    field_5: str | None = None  # 开工日期
    field_6: str | None = None  # 亮化效果
    field_7: str | None = None  # 项目状态

class RepairEntry(BaseModel):
    """报修单明细结构。"""

    field_0: str | None = None  # 报修编号
    field_1: str | None = None  # 报修位置
    field_2: str | None = None  # 故障类型
    field_3: str | None = None  # 报修人
    field_4: str | None = None  # 报修时间
    field_5: str | None = None  # 派修人员
    field_6: str | None = None  # 修复时间
    field_7: str | None = None  # 报修状态

class MeterEntry(BaseModel):
    """电表读数明细结构。"""

    field_0: str | None = None  # 电表编号
    field_1: str | None = None  # 所属配电箱
    field_2: str | None = None  # 抄表日期
    field_3: str | None = None  # 有功电量
    field_4: str | None = None  # 无功电量
    field_5: str | None = None  # 表底读数
    field_6: str | None = None  # 采集方式
    field_7: str | None = None  # 数据状态

class CableEntry(BaseModel):
    """电缆明细结构。"""

    field_0: str | None = None  # 电缆编号
    field_1: str | None = None  # 敷设方式
    field_2: str | None = None  # 电缆型号
    field_3: str | None = None  # 起点位置
    field_4: str | None = None  # 终点位置
    field_5: str | None = None  # 电缆长度
    field_6: str | None = None  # 敷设日期
    field_7: str | None = None  # 电缆状态

class AntiTheftEntry(BaseModel):
    """防盗设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 安装位置
    field_2: str | None = None  # 设备类型
    field_3: str | None = None  # 安装日期
    field_4: str | None = None  # 上次测试日期
    field_5: str | None = None  # 灵敏度等级
    field_6: str | None = None  # 报警方式
    field_7: str | None = None  # 设备状态

class AcceptanceEntry(BaseModel):
    """验收单明细结构。"""

    field_0: str | None = None  # 验收编号
    field_1: str | None = None  # 验收对象
    field_2: str | None = None  # 移交单位
    field_3: str | None = None  # 接收单位
    field_4: str | None = None  # 验收日期
    field_5: str | None = None  # 验收人员
    field_6: str | None = None  # 遗留问题
    field_7: str | None = None  # 验收结果

class ScheduleEntry(BaseModel):
    """开关灯方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 适用路段
    field_2: str | None = None  # 季节类型
    field_3: str | None = None  # 开灯时间
    field_4: str | None = None  # 关灯时间
    field_5: str | None = None  # 午夜减半时间
    field_6: str | None = None  # 执行日期
    field_7: str | None = None  # 方案状态

class ControllerEntry(BaseModel):
    """终端设备明细结构。"""

    field_0: str | None = None  # 终端编号
    field_1: str | None = None  # 终端型号
    field_2: str | None = None  # 安装位置
    field_3: str | None = None  # 通信协议
    field_4: str | None = None  # SIM卡号
    field_5: str | None = None  # 在线状态
    field_6: str | None = None  # 固件版本
    field_7: str | None = None  # 终端状态

class EmergencyEntry(BaseModel):
    """保障任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 保障类型
    field_2: str | None = None  # 保障区域
    field_3: str | None = None  # 开始时间
    field_4: str | None = None  # 结束时间
    field_5: str | None = None  # 负责人
    field_6: str | None = None  # 参与人员
    field_7: str | None = None  # 保障状态

class PatrolEntry(BaseModel):
    """巡检记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 巡检路段
    field_2: str | None = None  # 巡检日期
    field_3: str | None = None  # 巡检人员
    field_4: str | None = None  # 应亮灯数
    field_5: str | None = None  # 实亮灯数
    field_6: str | None = None  # 亮灯率
    field_7: str | None = None  # 巡检状态

class PlanEntry(BaseModel):
    """改造项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 改造路段
    field_3: str | None = None  # 改造内容
    field_4: str | None = None  # 预算金额
    field_5: str | None = None  # 计划开工
    field_6: str | None = None  # 计划竣工
    field_7: str | None = None  # 项目状态

class LandscapeEntry(BaseModel):
    """景观照明设施明细结构。"""

    field_0: str | None = None  # 设施编号
    field_1: str | None = None  # 设施名称
    field_2: str | None = None  # 景观类型
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 光源种类
    field_5: str | None = None  # 控制方式
    field_6: str | None = None  # 投用日期
    field_7: str | None = None  # 设施状态

class ComplaintEntry(BaseModel):
    """投诉记录明细结构。"""

    field_0: str | None = None  # 投诉编号
    field_1: str | None = None  # 投诉来源
    field_2: str | None = None  # 投诉路段
    field_3: str | None = None  # 投诉内容
    field_4: str | None = None  # 投诉时间
    field_5: str | None = None  # 处理人
    field_6: str | None = None  # 办结时间
    field_7: str | None = None  # 处理状态
