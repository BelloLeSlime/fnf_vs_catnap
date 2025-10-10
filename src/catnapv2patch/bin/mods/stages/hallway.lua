
function onCreate()
	-- background shit
	makeLuaSprite('hallway', 'hallway', -950, -440);
	setScrollFactor('hallway', 0.9, 0.9);
	scaleObject('hallway', 1, 1)

	makeLuaSprite('darkness', 'darkness', -2500, -200);
	setScrollFactor('darkness', 0, 0);
	scaleObject('darkness', 1, 1);

	addLuaSprite('hallway', false);
	addLuaSprite('darkness', true);

end