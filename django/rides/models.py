from django.db import models


class Ride(models.Model):
    import_id = models.UUIDField()
    #import_file = 

    title = models.CharField(max_length=100)
    was_edited = models.BooleanField(default=False)

    started_at = models.FloatField()
    ended_at = models.FloatField()

    elevation_gain = models.FloatField()
    elevation_loss = models.FloatField()

# esc_average_speed
# esc_efficiency
# esc_top_speed
# esc_top_speed_latitude
# esc_top_speed_longitude
# esc_total_distance_meters
# flagged_for_deletion = None
# gps_average_speed
# gps_top_speed
# gps_top_speed_latitude
# gps_top_speed_longitude
# gps_total_distance_meters
# vehicle_data_compressed = False
