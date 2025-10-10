
function onCreate()
	-- background shit
	makeAnimatedLuaSprite('redgas', 'redgas', 515, 300);
	addAnimationByPrefix('redgas', 'redgas', 'redgas', 6, true);
	setScrollFactor('redgas', 0.9, 0.9);
	scaleObject('redgas', 2, 2);

	makeAnimatedLuaSprite('redgas2', 'redgas2', -875, -125);
	addAnimationByPrefix('redgas2', 'redgas2', 'redgas2', 6, true);
	setScrollFactor('redgas2', 0.9, 0.9);
	scaleObject('redgas2', 2, 2);

	makeAnimatedLuaSprite('insidepov', 'insidepov', -200, -300);
	addAnimationByPrefix('insidepov', 'insidepov', 'insidepov', 15, true)
	setScrollFactor('insidepov', 0.9, 0.9);
	scaleObject('insidepov', 1.5, 1.5);


	addLuaSprite('insidepov', false);
	addLuaSprite('redgas', true);
	addLuaSprite('redgas2', false);
end