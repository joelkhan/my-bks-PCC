import sys
from loguru import logger

# 移除默认的日志处理器
logger.remove()

# 添加新的日志处理器，输出到标准输出
logger.add(sys.stdout, level="TRACE", format="{time} {level} {message}")

# 不同级别的日志记录示例
logger.trace("This is a trace message.")
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.success("This is a success message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")




