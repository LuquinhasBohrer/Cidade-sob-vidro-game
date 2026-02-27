extends CharacterBody2D

@export var walk_speed: float = 120.0
@export var run_speed: float = 220.0
@export var sneak_speed: float = 60.0
@export var stamina_max: float = 100.0
@export var stamina_recovery_per_second: float = 20.0
@export var stamina_run_cost_per_second: float = 30.0

var stamina: float = stamina_max

func _physics_process(delta: float) -> void:
	var move_vector := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	var can_run := Input.is_action_pressed("run") and stamina > 0.0 and move_vector.length() > 0.0
	var target_speed := walk_speed

	if can_run:
		target_speed = run_speed
		stamina = maxf(0.0, stamina - stamina_run_cost_per_second * delta)
	else:
		stamina = minf(stamina_max, stamina + stamina_recovery_per_second * delta)

	velocity = move_vector * target_speed
	move_and_slide()
