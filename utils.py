class CogitareLabsPoseIDExtractor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pose_keypoint": ("POSE_KEYPOINT",),
            },
            "optional": {
                "person_number": ("INT", { "default": 0 }),
            }
        }

    RETURN_TYPES = ("STRING")
    RETURN_NAMES = ("pointids")
    FUNCTION = "detect_pointids"
    CATEGORY = "utils"

    def detect_pointids(self, pose_keypoint,  person_number=0):

        if len( pose_keypoint[0]["people"] ) <= 0:
            return ("", )

        pose_keypoints_2d = pose_keypoint[0]["people"][person_number]["pose_keypoints_2d"]
        added_keypoints = []
        current_keypoint = []
        for x in pose_keypoints_2d:
            current_keypoint.append(x)
            if len(current_keypoint) == 3:
                added_keypoints.append(current_keypoint)
                current_keypoint = []

        detected_keypoints = []
        for i, x in enumerate(added_keypoints):

            sum_x = (x[0] + x[1]) * x[2]
            if sum_x > 0 :
                detected_keypoints.append(i)

        detected_keypoints = ",".join(map(str, detected_keypoints))

        return (detected_keypoints,)

NODE_CLASS_MAPPINGS = {
    "CogitareLabsPoseIDExtractor": CogitareLabsPoseIDExtractor
}
