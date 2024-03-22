#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -----------------------------------------------------------------
# File: d:\code\Personal-Assistant\src\scheduler.py
# Created Date: 2024 03 22nd Friday, 3:13:30 pm
# Author: xiaocao  (wdjoys@gmail.com>)
# ----------
# Last Modified: 2024 03 22nd Friday, 5:58:34 pm
# Modified By: xiaocao  (wdjoys@gmail.com>)
# ----------
# Description:
#
# Copyright (c) 2024 llhy Enterprises by github/wdjoys, All Rights Reserved
# -----------------------------------------------------------------


import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class SchedulerHandler:
    def __init__(self) -> None:
        # 创建调度器对象
        self.scheduler = AsyncIOScheduler()

    def add_scheduler_job(self):
        self.scheduler.add_job()

    def remove__scheduler_job(self, job_id):
        self.scheduler.remove_job(job_id=job_id)

    async def scheduler_run(self):
        # 调度器启动
        self.scheduler.start()

        # 保持调度器持续运行
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            self.scheduler.shutdown()


def scheduler_run(global_device_data: dict):
    """调度器执行函数

    Args:
        global_device_data (_type_): 全局设备数据
    """
    my_scheduler_handler = SchedulerHandler()
    asyncio.run(my_scheduler_handler.scheduler_run())


if __name__ == "__main__":
    scheduler_run()
