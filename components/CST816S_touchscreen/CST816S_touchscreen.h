#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "CST816S.h"

namespace esphome {
namespace cst816s_touchscreen {

class CST816STouchScreen : public text_sensor::TextSensor, public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
};

}  // namespace cst816s_touchscreen
}  // namespace esphome
