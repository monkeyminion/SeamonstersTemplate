__author__ = 'Ian'

# __all__ = ["Nav6Protocol"]

# class Nav6Protocol(Enum):

PACKET_START_CHAR = '!'
PROTOCOL_FLOAT_LENGTH = 7
CHECKSUM_LENGTH = 2
TERMINATOR_LENGTH = 2

# Yaw/Pitch/Roll (YPR) Update Packet
# e.g., !y[yaw][pitch][roll][checksum][cr][lf]

MSGID_YPR_UPDATE = 'y'
YPR_UPDATE_MESSAGE_LENGTH = 34
#    where yaw, pitch, roll are floats
#	 where checksum is 2 ascii-bytes of HEX checksum (all bytes before checksum)

YPR_UPDATE_YAW_VALUE_INDEX = 2
YPR_UPDATE_PITCH_VALUE_INDEX = 9
YPR_UPDATE_ROLL_VALUE_INDEX = 16
YPR_UPDATE_COMPASS_VALUE_INDEX = 23
YPR_UPDATE_CHECKSUM_INDEX = 30
YPR_UPDATE_TERMINATOR_INDEX = 32

# Quaternion Update Packet - e.g.:
# !r[q1][q2][q3][q4][accelx][accely][accelz][magx][magy][magz][checksum][cr][lf]

MSGID_QUATERNION_UPDATE = 'q'
QUATERNION_UPDATE_MESSAGE_LENGTH = 53
QUATERNION_UPDATE_QUAT1_VALUE_INDEX = 2
QUATERNION_UPDATE_QUAT2_VALUE_INDEX = 6
QUATERNION_UPDATE_QUAT3_VALUE_INDEX = 10
QUATERNION_UPDATE_QUAT4_VALUE_INDEX = 14
QUATERNION_UPDATE_ACCEL_X_VALUE_INDEX = 18
QUATERNION_UPDATE_ACCEL_Y_VALUE_INDEX = 22
QUATERNION_UPDATE_ACCEL_Z_VALUE_INDEX = 26
QUATERNION_UPDATE_MAG_X_VALUE_INDEX = 30
QUATERNION_UPDATE_MAG_Y_VALUE_INDEX = 34
QUATERNION_UPDATE_MAG_Z_VALUE_INDEX = 38
QUATERNION_UPDATE_TEMP_VALUE_INDEX = 42
QUATERNION_UPDATE_CHECKSUM_INDEX = 49
QUATERNION_UPDATE_TERMINATOR_INDEX = 51

# Gyro/Raw Data Update packet
# e.g., g[gx][gy][gz][accelx][accely][accelz][magx][magy][magz][temp_c][cr][lf]

MSGID_GYRO_UPDATE = 'g'
GYRO_UPDATE_MESSAGE_LENGTH = 46
GYRO_UPDATE_GYRO_X_VALUE_INDEX = 2
GYRO_UPDATE_GYRO_Y_VALUE_INDEX = 6
GYRO_UPDATE_GYRO_Z_VALUE_INDEX = 10
GYRO_UPDATE_ACCEL_X_VALUE_INDEX = 14
GYRO_UPDATE_ACCEL_Y_VALUE_INDEX = 18
GYRO_UPDATE_ACCEL_Z_VALUE_INDEX = 22
GYRO_UPDATE_MAG_X_VALUE_INDEX = 26
GYRO_UPDATE_MAG_Y_VALUE_INDEX = 30
GYRO_UPDATE_MAG_Z_VALUE_INDEX = 34
GYRO_UPDATE_TEMP_VALUE_INDEX = 38
GYRO_UPDATE_CHECKSUM_INDEX = 42
GYRO_UPDATE_TERMINATOR_INDEX = 44

#  EnableStream Command Packet - e.g., !S[stream type][checksum][cr][lf]

MSGID_STREAM_CMD = 'S'
STREAM_CMD_MESSAGE_LENGTH = 9
STREAM_CMD_STREAM_TYPE_YPR = MSGID_YPR_UPDATE
STREAM_CMD_STREAM_TYPE_QUATERNION = MSGID_QUATERNION_UPDATE
# STREAM_CMD_STREAM_TYPE_RAW 			= MSGID_RAW_UPDATE
STREAM_CMD_STREAM_TYPE_INDEX = 2
STREAM_CMD_UPDATE_RATE_HZ_INDEX = 3
STREAM_CMD_CHECKSUM_INDEX = 5
STREAM_CMD_TERMINATOR_INDEX = 7

#  EnableStream Response Packet - e.g.:
# !s[stream type][gyro full scale range][accel full scale range][update rate hz][yaw_offset_degrees][q1/2/3/4 offsets][flags][checksum][cr][lf]

MSG_ID_STREAM_RESPONSE = 's'
STREAM_RESPONSE_MESSAGE_LENGTH = 46
STREAM_RESPONSE_STREAM_TYPE_INDEX = 2
STREAM_RESPONSE_GYRO_FULL_SCALE_DPS_RANGE = 3
STREAM_RESPONSE_ACCEL_FULL_SCALE_G_RANGE = 7
STREAM_RESPONSE_UPDATE_RATE_HZ = 11
STREAM_RESPONSE_YAW_OFFSET_DEGREES = 15
STREAM_RESPONSE_QUAT1_OFFSET = 22
STREAM_RESPONSE_QUAT2_OFFSET = 26
STREAM_RESPONSE_QUAT3_OFFSET = 30
STREAM_RESPONSE_QUAT4_OFFSET = 34
STREAM_RESPONSE_FLAGS = 38
STREAM_RESPONSE_CHECKSUM_INDEX = 42
STREAM_RESPONSE_TERMINATOR_INDEX = 44

NAV6_FLAG_MASK_CALIBRATION_STATE = 0x03
NAV6_CALIBRATION_STATE_WAIT = 0x00
NAV6_CALIBRATION_STATE_ACCUMULATE = 0x01
NAV6_CALIBRATION_STATE_COMPLETE = 0x02

# IMU_PROTOCOL_MAX_MESSAGE_LENGTH = RAW_UPDATE_MESSAGE_LENGTH