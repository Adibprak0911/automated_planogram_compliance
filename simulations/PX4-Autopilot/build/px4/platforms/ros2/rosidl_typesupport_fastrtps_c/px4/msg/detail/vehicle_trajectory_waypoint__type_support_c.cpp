// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from px4:msg/VehicleTrajectoryWaypoint.idl
// generated code does not contain a copyright notice
#include "px4/msg/detail/vehicle_trajectory_waypoint__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "px4/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "px4/msg/detail/vehicle_trajectory_waypoint__struct.h"
#include "px4/msg/detail/vehicle_trajectory_waypoint__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "px4/msg/detail/trajectory_waypoint__functions.h"  // waypoints

// forward declare type support functions
size_t get_serialized_size_px4__msg__TrajectoryWaypoint(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_px4__msg__TrajectoryWaypoint(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, px4, msg, TrajectoryWaypoint)();


using _VehicleTrajectoryWaypoint__ros_msg_type = px4__msg__VehicleTrajectoryWaypoint;

static bool _VehicleTrajectoryWaypoint__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _VehicleTrajectoryWaypoint__ros_msg_type * ros_message = static_cast<const _VehicleTrajectoryWaypoint__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: type
  {
    cdr << ros_message->type;
  }

  // Field name: waypoints
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, px4, msg, TrajectoryWaypoint
      )()->data);
    size_t size = 5;
    auto array_ptr = ros_message->waypoints;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  return true;
}

static bool _VehicleTrajectoryWaypoint__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _VehicleTrajectoryWaypoint__ros_msg_type * ros_message = static_cast<_VehicleTrajectoryWaypoint__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: type
  {
    cdr >> ros_message->type;
  }

  // Field name: waypoints
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, px4, msg, TrajectoryWaypoint
      )()->data);
    size_t size = 5;
    auto array_ptr = ros_message->waypoints;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_px4
size_t get_serialized_size_px4__msg__VehicleTrajectoryWaypoint(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _VehicleTrajectoryWaypoint__ros_msg_type * ros_message = static_cast<const _VehicleTrajectoryWaypoint__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name timestamp
  {
    size_t item_size = sizeof(ros_message->timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name type
  {
    size_t item_size = sizeof(ros_message->type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name waypoints
  {
    size_t array_size = 5;
    auto array_ptr = ros_message->waypoints;

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_px4__msg__TrajectoryWaypoint(
        &array_ptr[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static uint32_t _VehicleTrajectoryWaypoint__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_px4__msg__VehicleTrajectoryWaypoint(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_px4
size_t max_serialized_size_px4__msg__VehicleTrajectoryWaypoint(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: timestamp
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: waypoints
  {
    size_t array_size = 5;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_px4__msg__TrajectoryWaypoint(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = px4__msg__VehicleTrajectoryWaypoint;
    is_plain =
      (
      offsetof(DataType, waypoints) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _VehicleTrajectoryWaypoint__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_px4__msg__VehicleTrajectoryWaypoint(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_VehicleTrajectoryWaypoint = {
  "px4::msg",
  "VehicleTrajectoryWaypoint",
  _VehicleTrajectoryWaypoint__cdr_serialize,
  _VehicleTrajectoryWaypoint__cdr_deserialize,
  _VehicleTrajectoryWaypoint__get_serialized_size,
  _VehicleTrajectoryWaypoint__max_serialized_size
};

static rosidl_message_type_support_t _VehicleTrajectoryWaypoint__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_VehicleTrajectoryWaypoint,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, px4, msg, VehicleTrajectoryWaypoint)() {
  return &_VehicleTrajectoryWaypoint__type_support;
}

#if defined(__cplusplus)
}
#endif
