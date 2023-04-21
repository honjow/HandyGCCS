#!/sbin/python3
#-*- coding: utf-8 -*-
from time import sleep
from evdev import UInput, AbsInfo, ecodes as e

# 定义手柄事件
CONTROLLER_EVENTS = {
    e.EV_ABS: [
        (e.ABS_X, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_Y, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_Z, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_RX, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_RY, AbsInfo(0, -32768, 32767, 16, 128, 0)),
        (e.ABS_RZ, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_HAT0X, AbsInfo(0, -1, 1, 0, 0, 0)),
        (e.ABS_HAT0Y, AbsInfo(0, -1, 1, 0, 0, 0)),
    ],
    e.EV_KEY: {
        e.BTN_SOUTH: 0, # X键
        e.BTN_EAST: 0, # O键
        e.BTN_NORTH: 0, # 三角键
        e.BTN_WEST: 0, # 方块键
        e.BTN_TL: 0, # L1键
        e.BTN_TR: 0, # R1键
        e.BTN_SELECT: 0, # SELECT键
        e.BTN_START: 0, # START键
        e.BTN_THUMBL: 0, # 左摇杆按键
        e.BTN_THUMBR: 0, # 右摇杆按键
        e.BTN_MODE: 0, # PS键
        e.BTN_TRIGGER_HAPPY1: 0, # 触发器键
        e.BTN_TRIGGER_HAPPY2: 0, # 触发器键
        e.BTN_TRIGGER_HAPPY3: 0, # 触发器键
        e.BTN_TRIGGER_HAPPY4: 0, # 触发器键
        e.BTN_TRIGGER_HAPPY5: 0 # 触发器键
    }
}

# 模拟手柄事件的函数
def simulate_controller():
    # 创建模拟输入设备
    # ui_device = UInput(
    #         CONTROLLER_EVENTS,
    #         name='V Sony Interactive Entertainment Wireless Controller',
    #         bustype=0x3,
    #         vendor=0x54c,
    #         product=0x5c4,
    #         version=0x0111
    #         )

    # ui_device = UInput(
    #         CONTROLLER_EVENTS,
    #         name='V Microsoft X-Box One S pad',
    #         bustype=0x3,
    #         vendor=0x045e,
    #         product=0x02ea,
    #         version=0x0301
    #         )

    ui_device = UInput.from_device('/dev/input/event18', name='V Wireless Controller')
    
    # 无限循环，模拟手柄事件
    while True:
        # 模拟按键事件
        # ui_device.write(e.EV_KEY, e.BTN_EAST, 1)
        ui_device.syn()
        sleep(1)

        # ui_device.write(e.EV_KEY, e.BTN_EAST, 0)
        ui_device.syn()
        sleep(1)


simulate_controller()