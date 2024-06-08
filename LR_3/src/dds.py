from cyclonedds.domain import DomainParticipant
from cyclonedds.pub import DataWriter as Publisher
from cyclonedds.sub import DataReader as Subscriber
from cyclonedds.topic import Topic
from cyclonedds.idl import IdlStruct
from dataclasses import dataclass


# Определение структуры данных Pose
@dataclass
class Pose(IdlStruct):
    x: float  # Координата X
    y: float  # Координата Y

# Определение структуры данных KeyboardKey
@dataclass
class KeyboardKey(IdlStruct):
    key: int  # Код клавиши


# Создание объекта DomainParticipant
dp = DomainParticipant()

# Создание топика "KeyTopic" для обмена сообщениями типа KeyboardKey
KeyTopic = Topic(dp, "KeyTopic", KeyboardKey)

# Создание публикатора для топика KeyTopic
TurtlePublisher = Publisher(dp, KeyTopic)
