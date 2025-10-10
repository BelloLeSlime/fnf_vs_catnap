
function onCreate()
	-- background shit
	makeLuaSprite('Wall', 'Wall', -500, -400);
	setScrollFactor('Wall', 1, 1);
	scaleObject('Wall', 1, 0.8);
	
	makeLuaSprite('Floor', 'Floor', -1000, 460);
	setScrollFactor('Floor', 1, 1);
	scaleObject('Floor', 1.5, 1.4);

	makeLuaSprite('couch', 'couch', 220, 70);
	setScrollFactor('couch', 1, 1);
	scaleObject('couch', 1.1, 1.1);

	makeLuaSprite('redbear', 'redbear', 900, 115);
	setScrollFactor('redbear', 1, 1);
	scaleObject('redbear', 1.3, 1.3);
	
	makeLuaSprite('piggy', 'piggy', 1250, 159);
	setScrollFactor('piggy', 1, 1);
	scaleObject('piggy', 1.3, 1.3);

	makeAnimatedLuaSprite('Dogday', 'Dogday', 490, 120);
	addAnimationByPrefix('Dogday', 'Dogday', 'Dogday', 24, true);
	setScrollFactor('Dogday', 1, 1);
	scaleObject('Dogday', 1.15, 1.15);

	makeLuaSprite('chicken', 'chicken', -210, 138);
	setScrollFactor('chicken', 1, 1);
	scaleObject('chicken', 1.2, 1.2);

	makeLuaSprite('corn', 'corn', -690, 188);
	setScrollFactor('corn', 1, 1);
	scaleObject('corn', 2, 2);

	makeLuaSprite('smartass', 'smartass', 1190, 208);
	setScrollFactor('smartass', 1, 1);
	scaleObject('smartass', 2, 2);

	makeLuaSprite('greenbun', 'greenbun', 0, 158);
	setScrollFactor('greenbun', 1, 1);
	scaleObject('greenbun', 1.2, 1.2);

	makeLuaSprite('Filter', 'Filter', -2500, -200);
	setScrollFactor('Filter', 0, 0);
	scaleObject('Filter', 1, 1);

	makeLuaSprite('Black Filter', 'Black Filter', -1000, -1000);
	setScrollFactor('Black Filter', 1, 1);
	scaleObject('Black Filter', 2, 2);
	setProperty('Black Filter.alpha',0.62)

	makeLuaSprite('Purple', 'Black Filter', -1000, -1000);
	setScrollFactor('Purple', 1, 1);
	scaleObject('Purple', 2, 2);
        makeGraphic('Purple',1280,720,'301934')
	setProperty('Purple.alpha',0.62)



	addLuaSprite('Wall', false);
	addLuaSprite('Floor', false);
	addLuaSprite('chicken', false);
	addLuaSprite('couch', false);
	addLuaSprite('redbear', false);
    addLuaSprite('Dogday', false);
	addLuaSprite('piggy', false);
	addLuaSprite('greenbun', false);
	addLuaSprite('corn', true);	
	addLuaSprite('smartass', true);	
	addLuaSprite('Filter', true);
	addLuaSprite('Black Filter', true);
end