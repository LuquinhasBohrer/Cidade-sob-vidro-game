extends Node2D

@onready var player: CharacterBody2D = $Player
@onready var interaction_label: Label = $CanvasLayer/InteractionLabel

func _ready() -> void:
	interaction_label.text = "WASD mover | SHIFT correr | E interagir"

func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("interact"):
		interaction_label.text = "Anomalia detectada no setor da cupula..."
