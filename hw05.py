# Loads default set of integrations. Do not remove.
default_config:

# Load frontend themes from the themes folder
frontend:
  themes: !include_dir_merge_named themes

automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml

shell_command:
  led_red_on: "curl http://172.20.10.3:5000/red_on"
  led_red_off: "curl http://172.20.10.3:5000/red_off"
  led_green_on: "curl http://172.20.10.3:5000/green_on"
  led_green_off: "curl http://172.20.10.3:5000/green_off"