
function onCreate()
	-- background shit
	makeLuaSprite('WallAlt', 'WallAlt', -500, -400);
	setScrollFactor('WallAlt', 1, 1);
	scaleObject('WallAlt', 1, 0.8);
	
	makeLuaSprite('FloorAlt', 'FloorAlt', -1000, 460);
	setScrollFactor('FloorAlt', 1, 1);
	scaleObject('FloorAlt', 1.5, 1.4);

	makeLuaSprite('couchAlt', 'couchAlt', 220, 70);
	setScrollFactor('couchAlt', 1, 1);
	scaleObject('couchAlt', 1.1, 1.1);

	makeLuaSprite('redbear', 'redbear', 900, 115);
	setScrollFactor('redbear', 1, 1);
	scaleObject('redbear', 1.3, 1.3);
	
	makeLuaSprite('piggy', 'piggy', 1250, 159);
	setScrollFactor('piggy', 1, 1);
	scaleObject('piggy', 1.3, 1.3);

	makeAnimatedLuaSprite('DogdayAlt', 'DogdayAlt', 490, 120);
	addAnimationByPrefix('DogdayAlt', 'DogdayAlt', 'DogdayAlt', 24, true);
	setScrollFactor('DogdayAlt', 1, 1);
	scaleObject('DogdayAlt', 1.15, 1.15);

	makeLuaSprite('chicken', 'chicken', -210, 138);
	setScrollFactor('chicken', 1, 1);
	scaleObject('chicken', 1.2, 1.2);

	makeLuaSprite('corn', 'corn', -920, 188);
	setScrollFactor('corn', 1, 1);
	scaleObject('corn', 2, 2);

	makeLuaSprite('smartass', 'smartass', 1350, 208);
	setScrollFactor('smartass', 1, 1);
	scaleObject('smartass', 2, 2);

	makeLuaSprite('greenbun', 'greenbun', 0, 158);
	setScrollFactor('greenbun', 1, 1);
	scaleObject('greenbun', 1.2, 1.2);

	makeAnimatedLuaSprite('smoke', 'smoke', 565, 40);
	addAnimationByPrefix('smoke', 'smoke', 'smoke', 6, true);
	setScrollFactor('smoke', 1, 1);
	scaleObject('smoke', 1.25, 1.25);
	
	makeLuaSprite('FilterAlt', 'FilterAlt', -2500, -200);
	setScrollFactor('FilterAlt', 0, 0);
	scaleObject('FilterAlt', 1, 1);

	makeLuaSprite('Black Filter', 'Black Filter', -1000, -1000);
	setScrollFactor('Black Filter', 1, 1);
	scaleObject('Black Filter', 2, 2);
	setProperty('Black Filter.alpha',0.62)

	makeLuaSprite('Purple', 'Black Filter', -1000, -1000);
	setScrollFactor('Purple', 1, 1);
	scaleObject('Purple', 2, 2);
        makeGraphic('Purple',1280,720,'301934')
	setProperty('Purple.alpha',0.62)

	makeAnimatedLuaSprite('smoke2', 'smoke2', -580, 220);
	addAnimationByPrefix('smoke2', 'smoke2', 'smoke2', 6, true);
	setScrollFactor('smoke2', 1.1, 1.1);
	scaleObject('smoke2', 1.25, 1.25);



	addLuaSprite('WallAlt', false);
	addLuaSprite('FloorAlt', false);
	addLuaSprite('chicken', false);	
	addLuaSprite('couchAlt', false);
	addLuaSprite('redbear', false);
	addLuaSprite('DogdayAlt', false);
	addLuaSprite('piggy', false);
	addLuaSprite('greenbun', false);
	addLuaSprite('corn', false);	
	addLuaSprite('smartass', false);	
	addLuaSprite('smoke', false);
	addLuaSprite('FilterAlt', true);
	addLuaSprite('Black Filter', true);
	addLuaSprite('smoke2', true);
end