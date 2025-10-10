
function onCreate()
	-- background shit
	makeLuaSprite('altWallother', 'altWallother', -500, -400);
	setScrollFactor('altWallother', 0.9, 0.9);
	scaleObject('altWallother', 1, 0.8);
	
	makeLuaSprite('Floorother', 'Floorother', -1000, 460);
	setScrollFactor('Floorother', 0.9, 0.9);
	scaleObject('Floorother', 1.5, 1.4);

	makeLuaSprite('couchother', 'couchother', 220, 70);
	setScrollFactor('couchother', 0.9, 0.9);
	scaleObject('couchother', 1.1, 1.1);

	makeAnimatedLuaSprite('daybear', 'daybear', 1100, 130);
    addAnimationByPrefix('daybear', 'daybear', 'daybear', 5, true)
    setScrollFactor('daybear', 0.9, 0.9);
	scaleObject('daybear', 1.3, 1.3);

	makeAnimatedLuaSprite('daypiggy', 'daypiggy', 1300, 189);
    addAnimationByPrefix('daypiggy', 'daypiggy', 'daypiggy', 5, true)
    setScrollFactor('daypiggy', 0.9, 0.9);
	scaleObject('daypiggy', 1.3, 1.3);

	makeAnimatedLuaSprite('daychicken', 'daychicken', -210, 138);
    addAnimationByPrefix('daychicken', 'daychicken', 'daychicken', 5, true)
    setScrollFactor('daychicken', 0.9, 0.9);
	scaleObject('daychicken', 1.15, 1.15);

	makeLuaSprite('nroc', 'nroc', -790, 188);
	setScrollFactor('nroc', 0.9, 0.9);
	scaleObject('nroc', 2, 2);

	makeLuaSprite('alien', 'alien', 1290, 208);
	setScrollFactor('alien', 0.9, 0.9);
	scaleObject('alien', 2, 2);

	makeAnimatedLuaSprite('daygreenbun', 'daygreenbun', 0, 128);
    addAnimationByPrefix('daygreenbun', 'daygreenbun', 'daygreenbun', 5, true)
    setScrollFactor('daygreenbun', 0.9, 0.9);
	scaleObject('daygreenbun', 1.3, 1.3);

	makeLuaSprite('Filterother', 'Filterother', -2500, -200);
	setScrollFactor('Filterother', 0, 0);
	scaleObject('Filterother', 1, 1);

	makeLuaSprite('Black Filter', 'Black Filter', -1000, -1000);
	setScrollFactor('Black Filter', 1, 1);
	scaleObject('Black Filter', 2, 2);
	setProperty('Black Filter.alpha',0.62)

	makeLuaSprite('Purple', 'Black Filter', -1000, -1000);
	setScrollFactor('Purple', 1, 1);
	scaleObject('Purple', 2, 2);
        makeGraphic('Purple',1280,720,'301934')
	setProperty('Purple.alpha',0.62)



	addLuaSprite('altWallother', false);
	addLuaSprite('Floorother', false);
	addLuaSprite('daychicken', false);
	addLuaSprite('couchother', false);
	addLuaSprite('daybear', false);
	addLuaSprite('daypiggy', false);
	addLuaSprite('daygreenbun', false);
	addLuaSprite('nroc', true);	
	addLuaSprite('alien', true);	
	addLuaSprite('Filterother', true);
	addLuaSprite('Black Filter', true);
end