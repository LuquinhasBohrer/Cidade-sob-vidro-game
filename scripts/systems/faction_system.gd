extends Node
class_name FactionSystem

const REPUTATION_MIN := -100
const REPUTATION_MAX := 100

var reputations := {
	"Conselho da Cupula": 0,
	"Subterraneos": 0,
	"Ordem do Vidro": 0,
	"Mercadores Livres": 0
}

func modify_reputation(faction_name: String, delta: int) -> void:
	if not reputations.has(faction_name):
		return

	reputations[faction_name] = clampi(reputations[faction_name] + delta, REPUTATION_MIN, REPUTATION_MAX)

func get_reputation_tier(faction_name: String) -> String:
	if not reputations.has(faction_name):
		return "Desconhecido"

	var value: int = reputations[faction_name]
	if value <= -61:
		return "Inimigo declarado"
	if value <= -31:
		return "Hostil"
	if value <= 30:
		return "Neutro"
	if value <= 60:
		return "Aliado"
	return "Campeao"
