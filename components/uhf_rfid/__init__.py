import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]

CONF_MQTT_TOPIC = 'mqtt_topic'

CONFIG_SCHEMA = cv.Schema({
    cv.Required(CONF_MQTT_TOPIC): cv.string,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
