import math # for functions like sqrt

# Perform an analysis of the sustainability of an action and return a percentage
# that represents on a scale of -100 to 100 how sustainable, environmentally,
# socially, and economically that thing is, based on how it meets the UN's
# standards for sustainable development (represented by the 17 SDGs as well as some
# core concepts that are addressed).

# Individual portions are analyzed separately and then weighted. A percentage is
# calculated by adding 100 to the score and dividing by 2. Each "section" goes
# from -100 to 100, but are multiplied by weighting factors (which add to 1)
# before summing to hold the final score within the acceptable scale.

def analyzeSustainability(action,
        coreWeight=0.4,
        environmentalWeight=0.3,
        societalWeight=0.2,
        economicWeight=0.1):
    # Environmental sustainability section
    # - refers to the environmental impact that the action has on the world,
    #   like pollution (or lack thereof), the usage of endangered resources/
    #   animals, etc.

    environmentalUnweighted = 0
    environmentalWeighted = environmentalUnweighted * environmentalWeight

    # Societal sustainability section
    # - refers to the societal impact that the action has on the world, such as
    #   inclusivity (or discrimination), the way that it affects poverty and
    #   education, etc.

    societalUnweighted = 0
    societalWeighted = societalUnweighted * societalWeight

    # Economic sustainability section
    # - refers to the economic impact that the action has on the world, such as
    #   creation (or destruction) of jobs, the equal opportunities thereof, etc.

    economicUnweighted = 0
    economicWeighted = economicUnweighted * economicWeight

    # Final score.

    score = environmentalWeighted + societalWeighted + economicUnweighted

    return score
