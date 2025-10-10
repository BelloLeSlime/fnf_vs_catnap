
function onCreate()
	-- background shit
	makeAnimatedLuaSprite('finalfog2', 'finalfog2', -235, 0);
	addAnimationByPrefix('finalfog2', 'finalfog2', 'finalfog2', 6, true);
	setScrollFactor('finalfog2', 0.9, 0.9);
	scaleObject('finalfog2', 1.3, 1.3);

	makeAnimatedLuaSprite('finalfog', 'finalfog', -875, -225);
	addAnimationByPrefix('finalfog', 'finalfog', 'finalfog', 5, true);
	setScrollFactor('finalfog', 0.9, 0.9);
	scaleObject('finalfog', 2, 2);

	makeLuaSprite('lastdestination', 'lastdestination', -500, -350);
	setScrollFactor('lastdestination', 0.9, 0.9);
	scaleObject('lastdestination', 2.5, 2.5);


	addLuaSprite('lastdestination', false);
	addLuaSprite('finalfog2', true);
	addLuaSprite('finalfog', false);
end