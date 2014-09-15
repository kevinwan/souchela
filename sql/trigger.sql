
# carsource_car_source表，自动填补classification字段
CREATE TRIGGER update_classification BEFORE INSERT ON carsource_car_source
FOR EACH ROW
BEGIN
  SELECT classification INTO @classification FROM carmodel_model WHERE slug=NEW.model_slug;
  SET NEW.classification = @classification;
END;
