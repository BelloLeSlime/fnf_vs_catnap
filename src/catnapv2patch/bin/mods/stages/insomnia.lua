
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

	makeLuaSprite('altbear', 'altbear', 900, 115);
	setScrollFactor('altbear', 1, 1);
	scaleObject('altbear', 1.3, 1.3);
	
	makeLuaSprite('altoink', 'altoink', 1250, 159);
	setScrollFactor('altoink', 1, 1);
	scaleObject('altoink', 1.3, 1.3);

	makeLuaSprite('altchicken', 'altchicken', -210, 138);
	setScrollFactor('altchicken', 1, 1);
	scaleObject('altchicken', 1.2, 1.2);

	makeLuaSprite('altcorn', 'altcorn', -920, 188);
	setScrollFactor('altcorn', 1, 1);
	scaleObject('altcorn', 2, 2);

	makeLuaSprite('altnerd', 'altnerd', 1350, 208);
	setScrollFactor('altnerd', 1, 1);
	scaleObject('altnerd', 2, 2);

	makeLuaSprite('altbun', 'altbun', 0, 158);
	setScrollFactor('altbun', 1, 1);
	scaleObject('altbun', 1.2, 1.2);

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
	addLuaSprite('altchicken', false);	
	addLuaSprite('couchAlt', false);
	addLuaSprite('altbear', false);
	addLuaSprite('altoink', false);
	addLuaSprite('altbun', false);
	addLuaSprite('altcorn', false);	
	addLuaSprite('altnerd', false);		
	addLuaSprite('smoke', false);
	addLuaSprite('FilterAlt', true);
	addLuaSprite('Black Filter', true);
	addLuaSprite('smoke2', true);
end