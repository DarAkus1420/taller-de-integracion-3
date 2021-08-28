class Config:
	pass

class DevelopmentConfig(Config):
	pass

class TestConfig(Config):
	pass

class ProductionConfig(Config):
	pass

config = {
	'test': TestConfig,
	'development': DevelopmentConfig
}