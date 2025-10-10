
function onCreate()
	-- background shit
	makeLuaSprite('smokyhallway', 'smokyhallway', -950, -440);
	setScrollFactor('smokyhallway', 0.9, 0.9);
	scaleObject('smokyhallway', 1, 1)

	makeLuaSprite('darkness', 'darkness', -2500, -200);
	setScrollFactor('darkness', 0, 0);
	scaleObject('darkness', 1, 1);

	addLuaSprite('smokyhallway', false);

end