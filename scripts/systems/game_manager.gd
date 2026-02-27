extends Node

@onready var faction_system: FactionSystem = $FactionSystem

func _ready() -> void:
	print("Cidade Sob Vidro - prototipo inicial carregado")
	print("Reputacao inicial Conselho: %s" % faction_system.get_reputation_tier("Conselho da Cupula"))
