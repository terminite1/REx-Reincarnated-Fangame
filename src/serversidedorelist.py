import json
blocks = [
    {'name': 'stone', 'rarity': 1/1},
    {'name': 'drycicle', 'rarity': 1/5},
    {'name': 'placeholder', 'rarity': 1/7},
    {'name': 'placeholder 2', 'rarity': 1/7.1},
    {'name': '1 whole byte', 'rarity': 1/12},
    {'name': 'the ore', 'rarity': 1/23},
    {'name': 'Not So Rare Stone', 'rarity': 1/25},
    {'name': 'iron', 'rarity': 1/55},
    {'name': 'Not So Rare Iron', 'rarity': 1/60},
    {'name': 'Potassium V6', 'rarity': 1/65},
    {'name': 'gold', 'rarity': 1/100},
    {'name': '2 whole bytes', 'rarity': 1/144},
    {'name': 'poop (regular)', 'rarity': 1/250},
    {'name': 'emerald', 'rarity': 1/340},
    {'name': 'sapphire', 'rarity': 1/500},
    {'name': 'your kitchen', 'rarity': 1/500},
    {'name': 'diamond', 'rarity': 1/680},
    {'name': 'ruby', 'rarity': 1/800},
    {'name': 'Yieeyj', 'rarity': 1/999},
    {'name': 'amethyst', 'rarity': 1/1000},
    {'name': 'topaz', 'rarity': 1/1200},
    {'name': 'platinum', 'rarity': 1/1280},
    {'name': 'obsidian', 'rarity': 1/1500},
    {'name': '1 whole kilobyte', 'rarity': 1/1500},
    {'name': '3 whole bytes', 'rarity': 1/1728},
    {'name': 'adamantium', 'rarity': 1/2000},
    {'name': 'uranium', 'rarity': 1/2500},
    {'name': 'quartz', 'rarity': 1/3000},
    {'name': 'neptunium', 'rarity': 1/4000},
    {'name': 'Flushing Bite', 'rarity': 1/4994},
    {'name': 'plutonium', 'rarity': 1/5000},
    {'name': 'flaming minion', 'rarity': 1/5232},
    {'name': 'Flaming Water', 'rarity': 1/5444},
    {'name': 'neutronium', 'rarity': 1/6000},
    {'name': 'gilded', 'rarity': 1/10000},
    {'name': 'ultrakillium', 'rarity': 1/10001},
    {'name': 'chicken ore', 'rarity': 1/15000},
    {'name': 'penny', 'rarity': 1/19999},
    {'name': 'thing', 'rarity': 1/20000},
    {'name': 'coffee creamer', 'rarity': 1/23000},
    {'name': 'ball', 'rarity': 1/25000},
    {'name': 'cube', 'rarity': 1/30000},
    {'name': 'dodecahedron', 'rarity': 1/33333},
    {'name': 'tricycle', 'rarity': 1/33333},
    {'name': 'Insizzlium', 'rarity': 1/34300},
    {'name': 'tesseract', 'rarity': 1/40000},
    {'name': 'fatassium', 'rarity': 1/44444},
    {'name': 'hypercube', 'rarity': 1/45000},
    {'name': 'spinning thing', 'rarity': 1/50000},
    {'name': 'cylinder', 'rarity': 1/55000},
    {'name': 'invisible staircase', 'rarity': 1/55445},
    {'name': 'Messier (REDACTED)', 'rarity': 1/56500},
    {'name': 'sphere', 'rarity': 1/60000},
    {'name': 'literally the number 6', 'rarity': 1/60000},
    {'name': 'dinosaur', 'rarity': 1/60000},
    {'name': 'dinosaur egg', 'rarity': 1/65000},
    {'name': 'dinosaur bone', 'rarity': 1/70000},
    {'name': 'dinosaur fossil', 'rarity': 1/75000},
    {'name': 'super flart', 'rarity': 1/77777},
    {'name': 'dinosaur poop', 'rarity': 1/80000},
    {'name': 'dinosaur meat', 'rarity': 1/85000},
    {'name': 'dinosaur skin', 'rarity': 1/90000},
    {'name': 'dinosaur blood', 'rarity': 1/95000},
    {'name': 'alexandrite', 'rarity': 1/100000},
    {'name': 'poudretteite', 'rarity': 1/125000},
    {'name': 'musgravite', 'rarity': 1/150000},
    {'name': 'benitoite', 'rarity': 1/150000},
    {'name': 'red beryl', 'rarity': 1/175000},
    {'name': 'grandidierite', 'rarity': 1/200000},
    {'name': 'black opal', 'rarity': 1/200000},
    {'name': 'Cryotic (not cave exclusive anymore)', 'rarity': 1/206000},
    {'name': 'jeremejevite', 'rarity': 1/225000},
    {'name': 'Ultremer 50', 'rarity': 1/234568},
    {'name': 'F25 key', 'rarity': 1/252525},
    {'name': 'albino fart', 'rarity': 1/300000},
    {'name': 'painite', 'rarity': 1/400000},
    {'name': 'Spectral Farts', 'rarity': 1/434343},
    {'name': 'diamond ore', 'rarity': 1/450000},
    {'name': 'tanzanite', 'rarity': 1/500000},
    {'name': 'Legacy Quasar Quasar Quasar 160529 618 618 V', 'rarity': 1/500000},
    {'name': 'ElectrolEDMiDeathinium', 'rarity': 1/545456},
    {'name': 'taaffeite', 'rarity': 1/600000},
    {'name': 'Robuxian', 'rarity': 1/666333},
    {'name': 'beryl', 'rarity': 1/700000},
    {'name': 'cool lookin pebble', 'rarity': 1/750000},
    {'name': 'HyperTesseract', 'rarity': 1/777888},
    {'name': 'jadeite', 'rarity': 1/800000},
    {'name': 'red diamond', 'rarity': 1/900000},
    {'name': 'jakpot 72', 'rarity': 1/999999},
    {'name': 'serendibite', 'rarity': 1/1000000},
    {'name': 'blue garnet', 'rarity': 1/1000000},
    {'name': 'kyawthuite', 'rarity': 1/1000000},
    {'name': 'cool diamond', 'rarity': 1/1000001},
    {'name': 'cool emerald', 'rarity': 1/1000001},
    {'name': 'cool sapphire', 'rarity': 1/1000001},
    {'name': 'cool ruby', 'rarity': 1/1000001},
    {'name': 'netherine', 'rarity': 1/1250000},
    {'name': 'enderite', 'rarity': 1/1500000},
    {'name': 'bedrock', 'rarity': 1/1750000},
    {'name': 'bedrockium', 'rarity': 1/2000000},
    {'name': 'bedrockite', 'rarity': 1/2250000},
    {'name': 'roentgenium', 'rarity': 1/2250001},
    {'name': 'Legacy Robuxian', 'rarity': 1/2403040},
    {'name': 'roxanite', 'rarity': 1/2500000},
    {'name': 'cool lookin ball', 'rarity': 1/2750000},
    {'name': 'cool lookin cube', 'rarity': 1/3000000},
    {'name': 'piepypi', 'rarity': 1/3141592},
    {'name': 'cool lookin dodecahedron', 'rarity': 1/3250000},
    {'name': 'cool lookin tricycle', 'rarity': 1/3500000},
    {'name': 'cool lookin tricycle 2', 'rarity': 1/3500000},
    {'name': 'quadrical', 'rarity': 1/3750000},
    {'name': 'spectral hole', 'rarity': 1/3750000},
    {'name': 'manganese', 'rarity': 1/5000000},
    {'name': 'guga leaf', 'rarity': 1/5500000},
    {'name': 'Ionizer581', 'rarity': 1/5810000},
    {'name': 'CAR HORN V878', 'rarity': 1/5888499},
    {'name': 'My China', 'rarity': 1/8888888},
    {'name': 'ADRENALINE', 'rarity': 1/10000000},
    {'name': 'Arccentuate', 'rarity': 1/22000000},
    {'name': 'Juicer 618', 'rarity': 1/61800000},
    {'name': 'Genuinium+Accesinite+Fire Crystal+Pandorite Fusion 72', 'rarity': 1/77787778},
    {'name': 'legacy blackhole 1236', 'rarity': 1/123600000},
    {'name': 'Lost RGB Sharkite Lamp ft. Stormal', 'rarity': 1/444444444},
    {'name': 'blutoof devious', 'rarity': 1/543277998},
    {'name': 'JPineJPhrine', 'rarity': 1/555555555},
    {'name': 'petrified wood 2', 'rarity': 1/2147483647},
    {'name': 'NILNALNULNEL', 'rarity': 1/2333333333},
    {'name': 'Grand Quasar Legacy 5171 A 160529 1236 V HR', 'rarity': 1/23882811155},
    {'name': 'the', 'rarity': 1/17000000000000}
]

print(json.dumps(blocks, indent=4))