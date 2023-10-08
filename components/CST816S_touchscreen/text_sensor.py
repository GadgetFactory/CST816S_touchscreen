import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID

cst816s_touchscreen_ns = cg.esphome_ns.namespace('cst816s_touchscreen')
CST816STouchScreen = cst816s_touchscreen_ns.class_('CST816STouchScreen', text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = text_sensor.TEXT_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(CST816STouchScreen)
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield text_sensor.register_text_sensor(var, config)
    yield cg.register_component(var, config)
    cg.add_library(
            name="CST816S",
            repository="https://github.com/GadgetFactory/CST816S.git",
            version="1.1.1",
        )
