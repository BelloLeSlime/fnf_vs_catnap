
function onCreate()
	-- background shit
	makeLuaSprite('rejectwall', 'rejectwall', -300, -350);
	setScrollFactor('rejectwall', 0.9, 0.9);
	scaleObject('rejectwall', 1.5, 1.5);
	
	makeLuaSprite('rejectfloor', 'rejectfloor', -950, 150);
	setScrollFactor('rejectfloor', 0.9, 0.9);
	scaleObject('rejectfloor', 2.7, 2.7);



	addLuaSprite('rejectwall', false);
	addLuaSprite('rejectfloor', false);
end