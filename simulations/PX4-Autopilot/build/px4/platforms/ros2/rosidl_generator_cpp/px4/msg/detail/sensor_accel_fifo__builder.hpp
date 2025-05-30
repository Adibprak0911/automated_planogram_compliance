// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4:msg/SensorAccelFifo.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__SENSOR_ACCEL_FIFO__BUILDER_HPP_
#define PX4__MSG__DETAIL__SENSOR_ACCEL_FIFO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4/msg/detail/sensor_accel_fifo__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4
{

namespace msg
{

namespace builder
{

class Init_SensorAccelFifo_z
{
public:
  explicit Init_SensorAccelFifo_z(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  ::px4::msg::SensorAccelFifo z(::px4::msg::SensorAccelFifo::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_y
{
public:
  explicit Init_SensorAccelFifo_y(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_z y(::px4::msg::SensorAccelFifo::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_SensorAccelFifo_z(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_x
{
public:
  explicit Init_SensorAccelFifo_x(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_y x(::px4::msg::SensorAccelFifo::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_SensorAccelFifo_y(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_samples
{
public:
  explicit Init_SensorAccelFifo_samples(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_x samples(::px4::msg::SensorAccelFifo::_samples_type arg)
  {
    msg_.samples = std::move(arg);
    return Init_SensorAccelFifo_x(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_scale
{
public:
  explicit Init_SensorAccelFifo_scale(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_samples scale(::px4::msg::SensorAccelFifo::_scale_type arg)
  {
    msg_.scale = std::move(arg);
    return Init_SensorAccelFifo_samples(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_dt
{
public:
  explicit Init_SensorAccelFifo_dt(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_scale dt(::px4::msg::SensorAccelFifo::_dt_type arg)
  {
    msg_.dt = std::move(arg);
    return Init_SensorAccelFifo_scale(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_device_id
{
public:
  explicit Init_SensorAccelFifo_device_id(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_dt device_id(::px4::msg::SensorAccelFifo::_device_id_type arg)
  {
    msg_.device_id = std::move(arg);
    return Init_SensorAccelFifo_dt(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_timestamp_sample
{
public:
  explicit Init_SensorAccelFifo_timestamp_sample(::px4::msg::SensorAccelFifo & msg)
  : msg_(msg)
  {}
  Init_SensorAccelFifo_device_id timestamp_sample(::px4::msg::SensorAccelFifo::_timestamp_sample_type arg)
  {
    msg_.timestamp_sample = std::move(arg);
    return Init_SensorAccelFifo_device_id(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

class Init_SensorAccelFifo_timestamp
{
public:
  Init_SensorAccelFifo_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SensorAccelFifo_timestamp_sample timestamp(::px4::msg::SensorAccelFifo::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_SensorAccelFifo_timestamp_sample(msg_);
  }

private:
  ::px4::msg::SensorAccelFifo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4::msg::SensorAccelFifo>()
{
  return px4::msg::builder::Init_SensorAccelFifo_timestamp();
}

}  // namespace px4

#endif  // PX4__MSG__DETAIL__SENSOR_ACCEL_FIFO__BUILDER_HPP_
