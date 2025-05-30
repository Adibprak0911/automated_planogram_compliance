// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4:msg/FigureEightStatus.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__FIGURE_EIGHT_STATUS__BUILDER_HPP_
#define PX4__MSG__DETAIL__FIGURE_EIGHT_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4/msg/detail/figure_eight_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4
{

namespace msg
{

namespace builder
{

class Init_FigureEightStatus_z
{
public:
  explicit Init_FigureEightStatus_z(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  ::px4::msg::FigureEightStatus z(::px4::msg::FigureEightStatus::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_y
{
public:
  explicit Init_FigureEightStatus_y(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  Init_FigureEightStatus_z y(::px4::msg::FigureEightStatus::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_FigureEightStatus_z(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_x
{
public:
  explicit Init_FigureEightStatus_x(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  Init_FigureEightStatus_y x(::px4::msg::FigureEightStatus::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_FigureEightStatus_y(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_frame
{
public:
  explicit Init_FigureEightStatus_frame(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  Init_FigureEightStatus_x frame(::px4::msg::FigureEightStatus::_frame_type arg)
  {
    msg_.frame = std::move(arg);
    return Init_FigureEightStatus_x(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_orientation
{
public:
  explicit Init_FigureEightStatus_orientation(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  Init_FigureEightStatus_frame orientation(::px4::msg::FigureEightStatus::_orientation_type arg)
  {
    msg_.orientation = std::move(arg);
    return Init_FigureEightStatus_frame(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_minor_radius
{
public:
  explicit Init_FigureEightStatus_minor_radius(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  Init_FigureEightStatus_orientation minor_radius(::px4::msg::FigureEightStatus::_minor_radius_type arg)
  {
    msg_.minor_radius = std::move(arg);
    return Init_FigureEightStatus_orientation(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_major_radius
{
public:
  explicit Init_FigureEightStatus_major_radius(::px4::msg::FigureEightStatus & msg)
  : msg_(msg)
  {}
  Init_FigureEightStatus_minor_radius major_radius(::px4::msg::FigureEightStatus::_major_radius_type arg)
  {
    msg_.major_radius = std::move(arg);
    return Init_FigureEightStatus_minor_radius(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

class Init_FigureEightStatus_timestamp
{
public:
  Init_FigureEightStatus_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FigureEightStatus_major_radius timestamp(::px4::msg::FigureEightStatus::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_FigureEightStatus_major_radius(msg_);
  }

private:
  ::px4::msg::FigureEightStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4::msg::FigureEightStatus>()
{
  return px4::msg::builder::Init_FigureEightStatus_timestamp();
}

}  // namespace px4

#endif  // PX4__MSG__DETAIL__FIGURE_EIGHT_STATUS__BUILDER_HPP_
