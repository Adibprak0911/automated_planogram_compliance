// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4:msg/DifferentialPressure.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__DIFFERENTIAL_PRESSURE__TRAITS_HPP_
#define PX4__MSG__DETAIL__DIFFERENTIAL_PRESSURE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4/msg/detail/differential_pressure__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4
{

namespace msg
{

inline void to_flow_style_yaml(
  const DifferentialPressure & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: timestamp_sample
  {
    out << "timestamp_sample: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp_sample, out);
    out << ", ";
  }

  // member: device_id
  {
    out << "device_id: ";
    rosidl_generator_traits::value_to_yaml(msg.device_id, out);
    out << ", ";
  }

  // member: differential_pressure_pa
  {
    out << "differential_pressure_pa: ";
    rosidl_generator_traits::value_to_yaml(msg.differential_pressure_pa, out);
    out << ", ";
  }

  // member: temperature
  {
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << ", ";
  }

  // member: error_count
  {
    out << "error_count: ";
    rosidl_generator_traits::value_to_yaml(msg.error_count, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DifferentialPressure & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << "\n";
  }

  // member: timestamp_sample
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp_sample: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp_sample, out);
    out << "\n";
  }

  // member: device_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "device_id: ";
    rosidl_generator_traits::value_to_yaml(msg.device_id, out);
    out << "\n";
  }

  // member: differential_pressure_pa
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "differential_pressure_pa: ";
    rosidl_generator_traits::value_to_yaml(msg.differential_pressure_pa, out);
    out << "\n";
  }

  // member: temperature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << "\n";
  }

  // member: error_count
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error_count: ";
    rosidl_generator_traits::value_to_yaml(msg.error_count, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DifferentialPressure & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace px4

namespace rosidl_generator_traits
{

[[deprecated("use px4::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const px4::msg::DifferentialPressure & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4::msg::DifferentialPressure & msg)
{
  return px4::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4::msg::DifferentialPressure>()
{
  return "px4::msg::DifferentialPressure";
}

template<>
inline const char * name<px4::msg::DifferentialPressure>()
{
  return "px4/msg/DifferentialPressure";
}

template<>
struct has_fixed_size<px4::msg::DifferentialPressure>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4::msg::DifferentialPressure>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4::msg::DifferentialPressure>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4__MSG__DETAIL__DIFFERENTIAL_PRESSURE__TRAITS_HPP_
