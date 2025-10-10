function onCreate()
	setPropertyFromClass('GameOverSubstate', 'characterName', 'povbf'); --Character json file for the death animation
	setPropertyFromClass('GameOverSubstate', 'deathSoundName', 'scream'); --put in mods/sounds/
	setPropertyFromClass('GameOverSubstate', 'loopSoundName', 'unsettling'); --put in mods/music/
	setPropertyFromClass('GameOverSubstate', 'endSoundName', 'gameOverEnd'); --put in mods/music/
end