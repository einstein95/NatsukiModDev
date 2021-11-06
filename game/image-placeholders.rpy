image placeholder_natsuki neutral = "mod_assets/natsuki/placeholder_neutral.png"
image placeholder_natsuki plead = "mod_assets/natsuki/placeholder_plead.png"
image placeholder_natsuki sad = "mod_assets/natsuki/placeholder_sad.png"
image placeholder_natsuki smile = "mod_assets/natsuki/placeholder_smile.png"
image placeholder_natsuki sparkle = "mod_assets/natsuki/placeholder_sparkle.png"
image placeholder_natsuki unamused = "mod_assets/natsuki/placeholder_unamused.png"
image placeholder_natsuki wink = "mod_assets/natsuki/placeholder_wink.png"

image placeholder_sky_day = "mod_assets/backgrounds/placeholder_sky_day.png"

define ease_transition = MoveTransition(0.1)

init 0 python in jn_placeholders:
    import store

    NATSUKI_Z_INDEX = 3
    SKY_Z_INDEX = 0

    def show_greeting_placeholder_natsuki():
        """
        Shows a resting Natsuki placeholder sprite based on current affinity.
        """
        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.ENAMORED:
            renpy.show(name="placeholder_natsuki smile", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.ease_transition)

        elif store.jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            renpy.show(name="placeholder_natsuki neutral", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.ease_transition)

        elif store.jn_affinity.get_affinity_state() >= store.jn_affinity.DISTRESSED:
            renpy.show(name="placeholder_natsuki unamused", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.ease_transition)

        else:
            renpy.show(name="placeholder_natsuki sad", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
            renpy.with_statement(trans=store.ease_transition)

    def show_resting_placeholder_natsuki(offset=False):
        """
        Shows the default resting Natsuki placeholder sprite, changing based on affinity level.

        IN:
            offset - Whether Natsuki should be drawn off to the left to account for menus, etc.

        """
        if store.jn_affinity.get_affinity_state() >= store.jn_affinity.NORMAL:
            if offset:
                renpy.show(name="placeholder_natsuki neutral", at_list=[store.left], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.ease_transition)

            else:
                renpy.show(name="placeholder_natsuki neutral", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.ease_transition)

        else:
            if offset:
                renpy.show(name="placeholder_natsuki sad", at_list=[store.left], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.ease_transition)

            else:
                renpy.show(name="placeholder_natsuki sad", at_list=[store.center], zorder=NATSUKI_Z_INDEX)
                renpy.with_statement(trans=store.ease_transition)
