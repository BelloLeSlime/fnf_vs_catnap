function onCreate()
	setPropertyFromClass('GameOverSubstate', 'characterName', 'kuddlebf'); --Character json file for the death animation
	setPropertyFromClass('GameOverSubstate', 'deathSoundName', ' '); --put in mods/sounds/
	setPropertyFromClass('GameOverSubstate', 'loopSoundName', ' '); --put in mods/music/
	setPropertyFromClass('GameOverSubstate', 'endSoundName', 'gameOverEnd'); --put in mods/music/
end